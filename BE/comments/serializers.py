from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user_id', 'recruit_id', 'post_id', 'content', 'to_user')

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'post_id', 'recruit_id')

    def validate(self, data):
        recruit_id = data.get('recruit_id')
        post_id = data.get('post_id')

        if not recruit_id and not post_id:
            raise serializers.ValidationError("ValidationError: recruit_id와 post_id 중 적어도 하나는 필요합니다.")

        # 유저는 현재 로그인한 사용자로 설정
        data['user_id'] = self.context['request'].user

        return data

class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']

    def validate(self, data):
        user = self.context['request'].user
        comment = self.instance

        if comment.user_id != user:
            raise serializers.ValidationError("댓글 작성자만 댓글을 수정할 수 있습니다.")

        return data

class CommentDeleteSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()

    def validate(self, data):
        comment_id = data.get('comment_id')
        user = self.context['request'].user

        try:
            comment = Comment.objects.get(pk=comment_id)
        except Comment.DoesNotExist:
            raise serializers.ValidationError("해당하는 댓글이 존재하지 않습니다.")

        if comment.user_id != user:
            raise serializers.ValidationError("댓글 작성자만 댓글을 삭제할 수 있습니다.")

        return data